#!/bin/bash

# example usage 
# . tools/mount_data.sh /home/gpss1/remote/datasets/GTA data/gta /home/gpss1/remote/datasets/GTA_curated_gtaids

ln -s "$1"/*images/images/* "$2"/images/
ln -s "$1"/*labels/labels/* "$2"/labels/

ln -sf "$3"/* "$2"/labels/

python3 tools/exclude_gta_images.py --dir "$2"

python3 tools/convert_datasets/gta.py "$2" --nproc 8
