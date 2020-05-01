---
title: Checking Compliance with Inspec
layout: post
date: '2020-05-01 05:00:00 -0500'
categories:
- Inspec
tags:
- Inspec
- Compliance
- STIG
- Security
---

# May 8th 2020

![Inspec Logo](https://github.com/inspec/inspec/raw/master/www/source/images/inspec-by-chef-logo.png)

* * *
# Content

***
# Intro to Inspec  

## What is Inspec?  
Chef Inspec is an open-source framework for testing, validating and reporting on system compliance.  

- Compliance as code
- Cross-platform (Windows, Linux, Mac, etc...)
- Can be built into DevOps porcesses to automate compliance end-to-end
- Can output results in various formats (JSON, YAML, HTML, etc...)

### Why do I care?  
Inspec can help you check the compliance of a system against a STIG or other compliance standard without having to install anything on the remote system. The results can then be easily viewed, prossed, or imported into standard tools.

### Why not just use SCAP?  

- SCAP benchmarks are very difficult to write and read.
- Updated benchmarks rarely exist for the solution that you need to check against or are out of date. 

### Inspec Basics  
#### Profiles  
Inspec Profiles are the "benchmarks" that you run on a system. An example of this would be something like a DISA STIG for Windows Server 2016 or Red Hat Enterprise Linux 7.  
``` 
examples/profile
├── README.md
├── controls
│   ├── example.rb
│   └── control_etc.rb
├── libraries
│   └── extension.rb
|── files
│   └── extras.conf
└── inspec.yml
```  

#### Controls and Resources
Inspec writes a check using what it calls controls. Controls can be written to use one of the many various Resources that exist out of the box. 

The below example would be a control that is use the **sshd_config** resource. 

``` ruby
control 'sshd-8' do
  impact 0.6
  title 'Server: Configure the service port'
  desc 'Always specify which port the SSH server should listen.'
  describe sshd_config do
    its('Port') { should cmp 22 }
  end
end
```
Additional out of the box resources can be found here -> [Inspec Resources](https://www.inspec.io/docs/reference/resources/)

#### Results
Results of a profile run can be seen when running a control or they can be saved to various formats. 

## Other Community Tools

### Heimdall
In addition to use the DISA STIG Viewer you can use MITRE's open source tool called Heimdall to view the results of an inspec profile. The tool also allows you to export the results to a CKL file directly in the application.

![Heimdall Demo](https://github.com/mitre/heimdall-lite/raw/master/public/heidmall-lite-2.0-demo-5fps.gif)

**Links:**  
[Heimdall Demo Environment](https://heimdall-demo.mitre.org/)  
[Heimdall Lite Repo](https://github.com/mitre/heimdall-lite)  
[Heimdall Full Repo](https://github.com/mitre/heimdall)  

### Inspec Tools
For DoD applications, the JSON output can be easily converted to a checklist (.CKL) file for use with the DISA STIG Viewer using MITRE's [Inspec Tools](https://inspec-tools.mitre.org/) utility.  

```
inspec_tools inspec2ckl -j results.json -o results.ckl
```

# Demos

## Basic Use
For simplicity I will use Chef's Learn Inspec Environment

1. Download the repo 
`git clone https://github.com/168cyber/inspec-demo`  
2. Start the environment  
`cd inspec-demo`  
`docker-compose up -d`
3. Connect to the "workstation" container  
`docker exec -it workstation bash`
4. Verify that the auditd package is not installed.  
`dpkg -s auditd | grep Status`
5. View the basic profile  
`tree /root/auditd`  
`cat /root/auditd/controls/example.rb`   
6. Run the profile against the worktation system locally. This will return a failure from Inspec.  
`inspec exec /root/auditd`  
7. Remediate this issue by installing auditd  
`apt-get install -y auditd`
8. Rerun the profile. This will return 1 success from Inspec.  
`inspec exec /root/auditd` 
9. Run it on a remote system.  
`inspec exec auditd -t ssh://root:password@target`  
10. Change the output to json  
`inspec exec auditd -t ssh://root:password@target --reporter=json | jq .`
11. Run a more complex profile directly from GitHub  
`inspec exec https://github.com/dev-sec/linux-baseline.git -t ssh://root:password@target` 

# Other Links
[Inspec](https://www.inspec.io)  
[Try Inspec](https://learn.chef.io/modules/try-inspec#/)  
[Dev-Sec](https://www.dev-sec.io)  
[MITRE GitHub](https://www.github.com/mitre) 
