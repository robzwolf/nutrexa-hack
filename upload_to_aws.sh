if [ -e Archive.zip ]
then
	rm Archive.zip
fi
zip Archive.zip lambda_function.py post_to_database.py read_from_database.py
aws lambda update-function-code --function-name New_Lambda --zip-file fileb:///Users/robbie/hackcambridge/nutrexa-hack/Archive.zip 
rm Archive.zip
