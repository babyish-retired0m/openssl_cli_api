# Openssl CLI api
Collect of useful commands for OpenSSL creating certificates, should be invoked on the command line.

# Requirements
`shell`
```
$ brew install openssl
```
# Usage

The recommended way to use OpenSSL CLI api is to use `python3`:

```
$ python3 start_main_api.py -a 4096
```
 
## Collect of useful command for OpenSSL create certificate:

**optional arguments:**

  - -h | --help            show this help message and exit
  
  - -a | --all [1024,2048,4096,8192,16392,32784,65568]
                        Create all Certificates, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568],
                        --all 4096
  - -c | --ca [1024,2048,4096,8192,16392,32784,65568]
                        Create CA certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784, 65568],
                        --ca 4096
  - -k | --key [1024,2048,4096,8192,16392,32784,65568]
                        Create key private certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784,
                        65568], --key 4096
  - -P | --p12 [1024,2048,4096,8192,16392,32784,65568]
                        Create key p12 certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784,
                        65568], --p12 4096
  - -p | --pub [1024,2048,4096,8192,16392,32784,65568]
                        Create key pub certificate, bit long modulus - choices=[1024, 2048, 4096, 8192, 16392, 32784,
                        65568], --pub 4096
  - -v, --version         show program's version number and exit
