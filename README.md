# git vtag
Simple and straightforward version tagging with Git. Version tags are tags in 
the following format:

      v<major>.<release>.<build>
     
(actually, the number of the components can be variable, we are only 
dealing with the last component)
  
## Installing
To install the released version:

      > pip install git-vtag

## Running
The command has built-in help:

      > git vtag

## Development version
To install the code in development mode:

      > git clone <git-repository-address>
      > cd git-vtag
      > python setup.py develop

**Tip**: if you are using virtual environment and autoenv, you may want to set up the .env file, for example:

    env_dir=./.venv
    echo activate $env_dir
    source $env_dir/bin/activate`
 
## Apache License
Copyright (C) 2016 **Sasha Ovsankin**

Licensed under the **Apache License, Version 2.0** (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

