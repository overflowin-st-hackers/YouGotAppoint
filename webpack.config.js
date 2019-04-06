let HTMLWebpackPlugin = require('html-webpack-plugin');
let miniCssExtractPlugin = require('mini-css-extract-plugin');
let path = require('path');
let devtools = '';

if(process.env.DEV_BUILD){
  devtools = 'source-map'
}

module.exports = {
    entry: './project/frontend/src/index.js',
    output:{
        filename: '[name].js',
        path: path.resolve(__dirname+'/project/frontend/static/frontend/')
    },
    devtool: devtools,
    module:{
        rules:[
            {
              test: /\.css$/,
              use: [
                {
                  loader: miniCssExtractPlugin.loader
                },
                {
                  loader: "css-loader",
                  options: {
                    sourceMap: true
                  }
                }
              ]
            },
            {
                test: /\.js$/,
                exclude: '/node_modules',
                use: [
                  {
                    loader: 'babel-loader',
                    options:{
                        presets: ['@babel/env','@babel/react']
                    }
                }]
            }
        ]
    },
    plugins: [
      new miniCssExtractPlugin({
          filename: '[name].css',
          chunkFilename: '[id].css'
      })
  ]
}