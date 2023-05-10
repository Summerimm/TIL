<template>
  <div>
    <h3 @click="goToDetail">{{ article.title }}</h3>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object
  },
  methods: {
    goToDetail() {
      const articleId = this.article.id
      this.$router.push({ name: 'DetailView', params: { id: articleId }})
    }
  }
}
</script>

<style>

</style>