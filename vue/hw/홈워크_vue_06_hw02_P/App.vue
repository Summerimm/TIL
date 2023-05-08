// App.vue

export default {
  name: 'App',
  created: function () {
    this.$store.dispatch('fetchTodoList')
  },
}