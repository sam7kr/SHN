// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.
const { remote } = require('electron')
const { BrowserWindow } = remote
const { PythonShell } = require('python-shell')


window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
        const element = document.getElementById(selector)
        if (element) element.innerText = text
    }

    for (const type of ['chrome', 'node', 'electron']) {
        replaceText(`${type}-version`, process.versions[type])
    }
  
    let pyshell = new PythonShell('pytest.py')
    pyshell.on('message', function(message){
    document.getElementById("divOne").innerText = message
  })

    pyshell.end(function (err, code, signal){
        if (err) throw err;
        console.log('exit code:' + code);
        console.log('exit signal:' + signal)
    }) 
    
})

