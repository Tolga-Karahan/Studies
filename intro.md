### Intro

go.mod files in each module tracks modules whose packages are imported in the code.
To enable dependency tracking  by creating a go.mod file,<br>following command must be
run:  

    go mod init <module-name>

Module name in the above command refers to the module path. In real cases it is 
mostly the repository location in which source code is maintained.<br>If code will be
published then it must be a location from which Go tools can download the module.

To run the code:

    go run .

To find published modules whose packages might have useful functions,  we should 
visit pkg.go.dev. When an external package is added to source code,<br>we should run
below command to add its module as a requirement to go.mod file:
  
    go mod tidy

When above command is run, it downloads the module by default it downloads the latest
version.
