const { spawn } = require('child_process');
const pyProg = spawn('python', ['module.py', 'Paul', 'arg2', 'argN']); // Passing arguments just for demo purposes
pyProg.stdout.on('data', function(data) {
    console.log(data.toString());
});
pyProg.stderr.on('data', function(data) {
    console.error(data.toString());
});
pyProg.on('close', function(code) {
    console.log(`Child process exited with code ${code}`);
});
