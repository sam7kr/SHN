// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.
const { remote } = require('electron')
const { BrowserWindow } = remote
const { PythonShell } = require('python-shell')


window.addEventListener('DOMContentLoaded', () => { 
    
    host = document.getElementById('host').value
    host = `'${host}'`
    function openPy(){
        let options = {
                scriptPath: '.',
                args:['192.168.1.10']
            }        
            let pyshell = new PythonShell('client.py', options)
            pyshell.on('message', function(message){
            document.getElementById("divOne").innerText = message
            })
            console.log(pyshell)
            console.log(host)
    
        function buttonOneOn(){
            console.log(`sending \'2on\' over tcp`)
            pyshell.send('2on')
        }

        function buttonOneOff(){
            console.log(`sending \'2off\' over tcp`)
            pyshell.send('2off')
        }

        function buttonTwoOn(){
            console.log(`sending \'3on\' over tcp`)
            pyshell.send('3on')
        }

        function buttonTwoOff(){
            console.log(`sending \'3off\' over tcp`)
            pyshell.send('3off')
        }

        function buttonKill(){
            console.log(`sending \'kill\' over tcp`)
            pyshell.send('kill')
            
        }

        function buttonBurn(){
            console.log(`sending \'burn\' over tcp`)
            pyshell.send('burn')
        }
        
        document.getElementById("buttonOneOn").addEventListener("click", buttonOneOn)
        document.getElementById("buttonOneOff").addEventListener("click", buttonOneOff)
        document.getElementById("buttonTwoOn").addEventListener("click", buttonTwoOn)
        document.getElementById("buttonTwoOff").addEventListener("click", buttonTwoOff)
        document.getElementById("kill").addEventListener("click", buttonKill)
        document.getElementById("burn").addEventListener("click", buttonBurn)
    }    

    document.getElementById("connectPy").addEventListener("click", openPy)
})

