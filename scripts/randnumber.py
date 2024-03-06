#!/usr/bin/env python3

import random
import boto3

def main():
    print("Showing random number between 1-5")
    print(random.randrange(1,5))