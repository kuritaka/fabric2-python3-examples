# Fabric2 Python3 Examples

## What is this
This is Fabric2 Examples with Python3

## Fabric2
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell commands remotely over SSH

http://www.fabfile.org/


## How to prepare

```
python3 -m pip -V    <- check version
python3 -m pip install --upgrade pip   <- pip upgrade
python3 -m pip -V    <- check version

pip search fabric
pip install fabric
```

```
git clone https://github.com/kuritaka/fabric2-python3-examples.git  fabric2
```

## How to use fabric
### one-line task examples
```
fab -H x.x.x.x --prompt-for-login-password -- hostname
fab -H x.x.x.x -- hostname
```


### task examples

```
fab -l    check lists

fab -H x.x.x  check_centos8
```
