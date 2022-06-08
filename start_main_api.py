#!/usr/bin/env python3
"""
Copyright 2022. All rights reserved.
"""
__version__ = "1.0"
import argparse
import os
import utilities.openssl as openssl
import utilities.file as file
import json
class Cli_api:
	"""
	usage
	"""
	def __init__(self, domain = "example.lan", bit = 4096, days = 256, algorithm = "sha256", parent_dir = os.path.dirname(__file__)):
		self.domain = domain
		self.bit = bit
		self.days = days
		self.algorithm =algorithm
		self.path = parent_dir + "/results/"
		
	
	def get_result(self, args):
		if args.all:
			print("\nCreating all Certificates:\n")
			self.Get_openssl = openssl.Create_Certificate(domain = self.domain, bit = self.bit, days = self.days, algorithm = self.algorithm, parent_dir = self.path)
			path = self.Get_openssl.All()
			config = json.load(open(path))
			print("\nConfig path:",path,"\n")
			print("CA password:",config["ca"]["private_key"]["password"])
			print("CA path:",config["ca"]["private_key"]["path"],"\n")
			print("KEY password:",config["key"]["private_key"]["password"])
			print("KEY path:",config["key"]["private_key"]["path"],"\n")
			print("p12 password:",config["key"]["p12"]["password"])
			print("p12 path:",config["key"]["p12"]["path"],"\n")
			print("Pub path:",config["key"]["pub"]["path"],"\n")
		if args.key_ca:
			print("Creating CA certificate")
			self.Get_openssl = openssl.Create_Certificate(domain = self.domain, bit = self.bit, days = self.days, algorithm = self.algorithm, parent_dir = self.path)
			path = self.Get_openssl.Key_CA()
			config = json.load(open(path))
			print("\nConfig path:",path,"\n")
			print("CA password:",config["ca"]["private_key"]["password"])
			print("CA path:",config["ca"]["private_key"]["path"],"\n")
		if args.key_private:
			print("Creating key private certificate")
			self.Get_openssl = openssl.Create_Certificate(domain = self.domain, bit = self.bit, days = self.days, algorithm = self.algorithm, parent_dir = self.path, key_signing = False)
			path = self.Get_openssl.Key_Private()
			config = json.load(open(path))
			print("\nConfig path:",path,"\n")
			print("KEY password:",config["key"]["private_key"]["password"])
			print("KEY path:",config["key"]["private_key"]["path"],"\n")
		if args.key_p12:
			print("Creating key p12 certificate")
			print(args)
			"""self.Get_openssl = openssl.Create_Certificate(domain = self.domain, bit = self.bit, days = self.days, algorithm = self.algorithm, parent_dir = self.path, key_signing = True)
			self.Get_openssl.Key_CA()
			self.Get_openssl.Key_Private()
			path = self.Get_openssl.Key_p12()
			config = json.load(open(path))
			print("\nConfig path:",path,"\n")
			print("CA password:",config["ca"]["private_key"]["password"])
			print("CA path:",config["ca"]["private_key"]["path"],"\n")
			print("KEY password:",config["key"]["private_key"]["password"])
			print("KEY path:",config["key"]["private_key"]["path"],"\n")
			print("p12 password:",config["key"]["p12"]["password"])
			print("p12 path:",config["key"]["p12"]["path"],"\n")"""
		if args.key_pub:
			print("Creating key pub certificate")
			print(args)
			self.Get_openssl = openssl.Create_Certificate(domain = self.domain, bit = self.bit, days = self.days, algorithm = self.algorithm, parent_dir = self.path, key_signing = False)
			self.Get_openssl.Key_Private()
			path = self.Get_openssl.Key_pub()
			config = json.load(open(path))
			print("\nConfig path:",path,"\n")
			print("KEY password:",config["key"]["private_key"]["password"])
			print("KEY path:",config["key"]["private_key"]["path"],"\n")
			print("Pub path:",config["key"]["pub"]["path"],"\n")
	def get_args(self, args = {}):
		self.parser = argparse.ArgumentParser(add_help = True, description = "Collect of useful command for OpenSSL create certificate:")
		group = self.parser.add_mutually_exclusive_group(required = True)
		group.add_argument("-a", "--all", dest = "all", default=False, type=int, choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], help = "Create all Certificates, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], --all 2048")
		group.add_argument("-c", "--ca", dest = "key_ca", default=False, type=int, choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], help = "Create CA certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], --ca 2048")
		group.add_argument("-k", "--key", dest = "key_private", default=False, type=int, choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], help = "Create key private certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], --key 2048")
		group.add_argument("-P", "--p12", dest = "key_p12", default=False, type=int, choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], help = "Create key p12 certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], --p12 2048")
		group.add_argument("-p", "--pub", dest = "key_pub", default=False, type=int, choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], help = "Create key pub certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568], --pub 2048")
		group.add_argument("-v", "--version", action="version", version="%(prog)s version: "+ __version__)
		args = self.parser.parse_args()
		return args
	
if __name__ == '__main__':
	import start_main_api
	import sys
	try:
		Openssl_cli_api = Cli_api(domain = "example.lan", bit = 2048)
		Openssl_cli_api.get_result(Openssl_cli_api.get_args(args = {}))
	except KeyboardInterrupt:
		print("{}Canceling script...{}\n".format("\033[33m", "\033[39m"))
		sys.exit(1)
