# usefulTools

Useful tools to get stats and look at tif images.
All scripts can be used as a bash command is the folder is added to the $PATH

- combineStack : combine two image stacks (USAGE : combineStack [imagePath] [imagePath2])
- cropImage : crop image in 128.128 patches (USAGE : cropImage [imagePath] [options])
- shiftTif : shift all images of a stack from n pixels on x and / or y axis  (USAGE : shiftTif [imagePath] [options])
- showPatches : quickly show 5 X and Y images of a npz stack patches (USAGE : showPatches [imagePath])
- showTif : show tif images with pyplot (USAGE : showTif [imagePath] [options])
- splitTif : split a tif stack in a smaller stack (USAGE : splitTif [imagePath] [options])

Each tool has a --help function for more information

# About
This toolbox has been developped to help building CSBDeep model (https://github.com/nriss/DatasetMicroscopy).
Developped by Nicolas Riss under the supervision of Julien Godet
