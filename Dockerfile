# Use an image that has Conda installed
FROM continuumio/miniconda3

# Install system dependencies
RUN apt-get update && apt-get install -y curl build-essential

# Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustup default stable

# Set a working directory
WORKDIR /usr/src/app

# Copy the project files into the working directory
COPY . .

# Create the Conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the Conda environment:
SHELL ["conda", "run", "-n", "penguins-env", "/bin/bash", "-c"]

# Activate the Conda environment
RUN /bin/bash -c "source activate penguins-env"

# Run the kedro pipeline preprocessing and modeling
RUN kedro run -p preprocessing
RUN kedro run -p modeling

EXPOSE 8000

#TODO Naprawić serving
#TODO odapić w kontenerze fastapi
# Start FastAPI using Uvicorn when the container launches
CMD /bin/bash -c "source activate penguins-env && python -m uvicorn main:app --port 8000 --host 0.0.0.0 --timeout-keep-alive 120"

