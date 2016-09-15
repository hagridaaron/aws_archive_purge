# aws_archive_purge

##Introduction
This is a script I wrote while planning the transition between physical tape backups and backups using Amazon's StorageGateway VTL service. For more informatino on Amazon StorageGateway or VTL checkout [This Page](https://aws.amazon.com/marketplace/pp/B015GTM1I8/ref=ads_1cc95292-d0b9-1473898216)

##Prerequisets 
This script presupposes that you have installed and configured the [AWS CLI](https://aws.amazon.com/cli/) for use with your AWS account. It also assumes that you've installed and configured the local StorageGateway on your own network for use with tapes. 

