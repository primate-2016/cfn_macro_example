import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(event, context):

    logger.info(f'Received event: {json.dumps(event, indent=2)}')

    # get the number of SSM params to output from the template parameters
    number_of_ssm_params = event['templateParameterValues']['NumberOfSsmParams']

    logger.info(f'Going to output {number_of_ssm_params} SSM parameters')

    # we will output some full CFN resources in a loop here
    for n in range(int(number_of_ssm_params)):
        event['fragment']['Resources'][f'SsmParam{n}'] = {
            'Type' : 'AWS::SSM::Parameter',
            'Properties' : {
                'Description' : f'This is the SSM param {n}',
                'Name' : f'/Cfn/MacroExample{n}',
                'Type' : 'String',
                'Value' : 'something exciting'
                }
            }

    # we can also update a specific bit of a resource in a template using a macro
    event['fragment']['Resources']['NormalSsmParam']['Properties']['Value'] = 'This was changed by the CFN Macro'

    logger.info(f'returning the following to CFN: {json.dumps(event)}')

    return {
        'requestId': event['requestId'],
        'status': 'success',
        'fragment': event['fragment']
    }