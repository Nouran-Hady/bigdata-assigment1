#!/bin/bash
 
# Create the output directory on the local machine if it doesn't exist
mkdir -p \service-result
cd \service-result
# Copy a file from a container to the current directory on your local machine
docker cp 59cfaa94fd34/://home/doc-bd-a1/vis.png .
docker cp 59cfaa94fd34/://home/doc-bd-a1/output_eda.csv .
docker cp 59cfaa94fd34/://home/doc-bd-a1/res_dpre.csv .
docker cp 59cfaa94fd34/://home/doc-bd-a1/eda-insight-1.txt .
docker cp 59cfaa94fd34/://home/doc-bd-a1/eda-insight-2.txt .
docker cp 59cfaa94fd34/://home/doc-bd-a1/eda-insight-3.txt .
docker cp 59cfaa94fd34/://home/doc-bd-a1/eda-insight-4.txt .

docker stop 59cfaa94fd34

# #!/bin/bash

# # Specify the Docker container name
# CONTAINER_ID=3e83d02ee9de

# # Define the local destination directory
# LOCAL_DESTINATION=D:/c lenovo/nu 2023/Big Data/assigment 1/bd-a1/service-result
# mkdir -p $LOCAL_DESTINATION
# # # Define the container source directories for the output files
# CONTAINER_SOURCES1=/eda-insight-1.txt
# CONTAINER_SOURCES2=/eda-insight-2.txt
# CONTAINER_SOURCES3=/eda-insight-3.txt
# CONTAINER_SOURCES4=/eda-insight-4.txt
# CONTAINER_SOURCES5=/k.txt
# CONTAINER_SOURCES6=/vis.png
# CONTAINER_SOURCES7=/res_dpre.csv

# # Copy the output files from the container to the local machine
# docker cp $CONTAINER_SOURCES1 $CONTAINER_ID: $LOCAL_DESTINATION
# docker cp $CONTAINER_ID: $CONTAINER_SOURCES2 $LOCAL_DESTINATION
# docker cp $CONTAINER_ID: $CONTAINER_SOURCES3 $LOCAL_DESTINATION
# docker cp $CONTAINER_ID: $CONTAINER_SOURCES4 $LOCAL_DESTINATION
# docker cp $CONTAINER_ID: $CONTAINER_SOURCES5 $LOCAL_DESTINATION
# docker cp $CONTAINER_ID: $CONTAINER_SOURCES6 $LOCAL_DESTINATION
# docker cp $CONTAINER_ID: $CONTAINER_SOURCES7 $LOCAL_DESTINATION
# # Stop and remove the Docker container
# echo kk
# # docker stop $CONTAINER_ID
# docker container stop $CONTAINER_ID
# # $ docker stop $(docker ps -q)
# echo finished