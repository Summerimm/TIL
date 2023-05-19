import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles: [],
  },
  getters: {
  },
  mutations: {
    SAVE_ARTICLES(state, articles){
      state.articles = articles
    }
  },
  actions: {
    fetchArticles(context) {
      // axios 요청을 보내야 하지만 받았다고 가정하고
      const articles = [
        {
          id: 1, 
          title: '제목',
          content: '내용',
        },
        {
          id: 2, 
          title: '제목2',
          content: '내용2',
        },
      ]
      context.commit('SAVE_ARTICLES', articles)
    }
  },
  modules: {
  }
})
