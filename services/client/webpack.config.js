const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const WebpackManifestPlugin = require('webpack-manifest-plugin')

module.exports = {
  entry: './src/index.jsx',
  output: {
    path: path.join(__dirname, '/public'),
    publicPath: '/',
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader', 'eslint-loader']
      },
      {
        test: /\.(css|sass|scss)$/i,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              url: true,
              import: true,
              importLoaders: 1,
              sourceMap: true
            }
          },
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true
            }
          }
        ]
      },
      {
        test: /\.svg$/,
        use: [
          {
            loader: 'babel-loader'
          },
          {
            loader: 'react-svg-loader',
            options: {
              jsx: true
            }
          }
        ]
      },
      {
        test: /\.json$/,
        loader: 'json-loader'
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx'],
    alias: {
      react: path.resolve('./node_modules/react')
    }
  },
  devServer: {
    contentBase: './public',
    port: 3000,
    host: '0.0.0.0',
    // ADD THIS LINE.
    historyApiFallback: true,
    watchOptions: {
      aggregateTimeout: 500,
      poll: 1000
    }
  },
  plugins: [
    new WebpackManifestPlugin({
      fileName: 'manifest.json',
      generate: (seed, files) => {
        const manifestFiles = files.reduce((manifest, file) => {
          manifest[file.name] = file.path
          return manifest
        }, seed)

        return {
          files: manifestFiles
        }
      }
    }),
    new HtmlWebpackPlugin({
      template: './public/index.html',
      favicon: './public/favicon.ico'
    })
  ]
}
