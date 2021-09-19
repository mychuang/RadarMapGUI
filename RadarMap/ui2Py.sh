#bin/bash

echo "ui file name is (don't include .ui):"
read uiForm
uiFile=$uiForm".ui"
echo "reading: "$uiFile

if [ -f $uiFile ]; then
  uipy="ui_"$uiForm".py"
  pyuic5 -o $uipy $uiFile

  if [ -f $uipy ]; then
     read -p "Parse sucessful!! Press key to exit..."
  else
     echo "Holy shit !"
  fi

else
  echo "file not found"
fi

