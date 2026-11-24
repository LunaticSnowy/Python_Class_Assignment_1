I'm passing dicts around a lot because I can't use OOP or classes nor do I want to use globals.
Dicts are the new C structs :D.

Type hinting is casting some errors in specific files. This is caused by the dict return types having the "possibility" to not align with the data types required when passed in certain functions. These errors are; as the name suggests, a hint. They aren't causing any issues.

The naming convention for the the folders & files isn't following pep8. I'll fix it for the next assignment.
I'm also planning to update file structure in a way that it's more "Python like" rather than the "C or Rust way" I've currently wrote it.

Program structure is:
    sensorMonitor ->
                    sensorInterface ->
                                      sensorAnalog -> helperRNG
                                      sensorIMU    -> helperRNG
                    sensorFile
                    sensorAnalysis
                    sensorVisualization