const FileManagerPlugin = require('filemanager-webpack-plugin-fixed');

module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

  devServer: {
    index: 'home.html',
    proxy: 'http://127.0.0.1:8000', //xhr only
  },

  outputDir: 'dist',
  publicPath: '/',
  assetsDir: 'static',

  pages: {

    home : {
      template: 'public/index.html',
      entry: 'src/pages/main_home.js',
      filename: 'home.html',
      title: 'blog/home.html',
      minify: false,
    },

    post_llist : {
      template: 'public/index.html',
      entry: 'src/pages/post_list.js',
      filename: 'post_list.html',
      title: 'blog/post_list.html',
      minify: false,
    },

    post_detail : {
      template: 'public/index.html',
      entry: 'src/pages/post_detail.js',
      filename: 'post_detail.html',
      title: 'blog/post_detail.html',
      minify: false,
    },
  },

  configureWebpack: {
    plugins: [
      new FileManagerPlugin({
        onStart: {
          delete: [
            '../backend/blogsite/static/**/',
            '../backend/blogsite/template/**/',
          ],
        },

        onEnd: {
          copy: [
            { source: 'dist/static', destination: '../backend/blogsite/static/'},
            { source: 'dist/favicon.ico', destination: '../backend/blogsite/static/img/'},
            { source: 'dist/home.html', destination: '../backend/blogsite/templates/'},
            { source: 'dist/post*.html', destination: '../backend/blogsite/templates/blog/'},
          ],
        }
      }),
    ]
  },
}
