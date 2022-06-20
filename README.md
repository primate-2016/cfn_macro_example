# cfn_macro_example
Unecessary CFN Macro example so that I don't forget how they work again.....

aws cloudformation package --template-file ./template.yml --s3-bucket *your_bucket_name* --output-template-file output.yaml

aws cloudformation deploy --template-file ./output.yaml --stack-name *stack_name* --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND