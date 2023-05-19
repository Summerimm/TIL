<template>
  <div>
    <h1>보고싶은 영화</h1>
    <p>
      <input type="text" v-model.trim="movieTitle">
      <button @click="createMovie" class="btn btn-success ms-2">Add</button>
    </p>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      movieTitle: null,
    }
  },
  methods: {
    createMovie() {
      if (this.movieTitle) {
        this.$store.dispatch('createMovie', this.movieTitle)
      } else {
        alert('영화 제목을 입력하세요!')
      }
      this.movieTitle = null
    }
  }
}
</script>

<style>

</style>