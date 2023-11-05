# Specify the base image as Ubuntu
FROM ubuntu

# Install required packages
# RUN apt-get install -y nano
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano
RUN pip install argparse
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container at /home/doc-bd-a1/
RUN mkdir -p /home/doc-bd-a1/

# Move the dataset file to the container
COPY CCGENERAL.csv  /home/doc-bd-a1/

# Set the working directory
WORKDIR  /home/doc-bd-a1/

# Open the bash shell upon container startup
CMD ["bash"]