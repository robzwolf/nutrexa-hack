echo
echo "Performing git pull..."
echo
git pull
echo
echo "Checking temp Archive.zip existence..."
echo
if [ -e Archive.zip ]
then
	echo "Archive.zip already exists."
	echo "Removing Archive.zip..."
	rm Archive.zip
	echo "Removed Archive.zip."
else
	echo "Archive.zip did not exist."
fi
echo "Doing zipping..."
echo
zip Archive.zip lambda_function.py post_to_database.py read_from_database.py
echo
echo "Made Archive.zip"
echo
echo "Uploading to AWS..."
aws lambda update-function-code --function-name New_Lambda --zip-file fileb:///Users/robbie/hackcambridge/nutrexa-hack/Archive.zip 
echo "Cleaning up..."
rm Archive.zip

echo
echo "----------"
echo "Completed!"
echo "----------"
