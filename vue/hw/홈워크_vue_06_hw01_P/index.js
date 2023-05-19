// store/index.js

export default new Vuex.Store({
  state: {
    count: 0,
  },
  mutations: {
    NUMBER_INCREMENT: function (state) {
      state.count++
    },
  },
  actions: {
    numberIncrement: function (context) {
      context.commit('NUMBER_INCREMENT')
    },
  },
})