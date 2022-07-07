const express = require('express')
const path = require('path')
const app = express()
const port = 3000

app.use(express.static(__dirname));

app.get('/en', (request, response) => {
    response.sendFile(path.join(__dirname, '/index.html'))
})

app.listen(port, (err) => {
    if (err) {
        return console.log('something bad happened', err)
    }
    console.log(`server is listening on ${port}`)
})


