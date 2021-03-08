module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

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
}
