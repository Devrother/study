const express = require('express')
const app = express()
const port = process.env.PORT || 3030

app.use(express.json())

app.listen(port, () => {
    console.log(`listening .. port : ${port}`)
})
