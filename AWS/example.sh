#!/bin/bash


https://aws.amazon.com/ko/getting-started/hands-on/backup-to-s3-cli/

S3KEY="my aws key"
S3SECRET="my aws secret" # pass these in


function putS3
{
  path=$1
  file=$2
  aws_path=$3
  bucket='my-aws-bucket'
  date=$(date +"%a, %d %b %Y %T %z")
  acl="x-amz-acl:public-read"
  content_type='application/x-compressed-tar'
  string="PUT\n\n$content_type\n$date\n$acl\n/$bucket$aws_path$file"
  signature=$(echo -en "${string}" | openssl sha1 -hmac "${S3SECRET}" -binary | base64)
  curl -X PUT -T "$path/$file" \
    -H "Host: $bucket.s3.amazonaws.com" \
    -H "Date: $date" \
    -H "Content-Type: $content_type" \
    -H "$acl" \
    -H "Authorization: AWS ${S3KEY}:$signature" \
    "https://$bucket.s3.amazonaws.com$aws_path$file"
}


twoBeforeStartDate=$(date -d "-1 month" '+%Y0101')
twoBeforeEndDate=$(date -d "-1 month" '+%Y%m31')
BashDuseApiFile="/var/www/duse-api/storage/logs"
BashPeterWebFile="/var/www/peter-web/storage/logs"
BashCeoFile="/var/www/ceo/storage/logs"
while [ "${twoBeforeStartDate}" -le "${twoBeforeEndDate}" ]
do
        BashTwoFileDate=$(date -d "${twoBeforeStartDate}" "+%Y-%m-%d")
        twoBeforeStartDate=$(date -d "${twoBeforeStartDate} + 1 day" "+%Y%m%d")
        cd ${BashDuseApiFile};
        BashFile="laravel-cli-${BashTwoFileDate}.tar.gz"
        if [ -f "${BashFile}" ]; then
                echo "${BashDuseApiFile}${BashFile}";
                
                for file in "$path"/*; do
                    putS3 "$path" "${file##*/}" "/path/on/s3/to/files/"
                done

                sudo rm -rf "${BashDuseApiFile}/${BashFile}"
        fi
        cd ${BashPeterWebFile};
        BashFile="laravel-cli-${BashTwoFileDate}.tar.gz"
        if [ -f "${BashFile}" ]; then
                echo "${BashPeterWebFile}${BashFile}";

                aws s3 mv ${BashFile} s3://bucket-name <--

                sudo rm -rf "${BashPeterWebFile}/${BashFile}"
        fi
done
