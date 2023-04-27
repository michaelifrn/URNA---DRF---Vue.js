<template>
  <div id="app">


    <div v-if="screenOutput != 'voted'" class="vote">

      <div class="urna">

        <screenOutput
        :reportList = "report"
        />

      </div>

      <div class="candidates">
        <screenCandidate
        :candidatesList = "candidatesList"
        />
      </div>

      <div class="candidates">
        <screenVotes
        :report = "report"
        />
      </div>

    </div>
  
  </div>
</template>

<script>

import '@/css/global.css'


import screenOutput from '@/components/screenOutput';

import screenCandidate from '@/components/screenCandidate'

import screenVotes from '@/components/screenVotes'

import functions from './services/candidates';

export default {
  name: 'App',
  mounted(){
    functions.list().then(respost => {
      this.candidatesList = respost.data
      console.log(this.candidatesList)
    }),

    functions.voteList().then(respost =>{
      this.votesList = respost.data
      console.log(this.votesList)
    }),
    
    functions.report().then(respost =>{
      this.report = respost.data
      console.log(this.report)
    })
  },
  components: {
    screenOutput,
    screenCandidate,
    screenVotes
  },
  methods:{
    changeScreen(){

      if (this.screenOutput == "registration")
      this.screenOutput = " "
    },

  },

  data(){
    return {
      candidatesList: [],
      votesList: [],
      report: []
      
    }
  }
}
</script>

<style>
#app {
  background-color: var(--background-color);
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 30px;
}

.urna {
  width: 700px;
  background-color: var(--ballot-box-background-color);
  padding: 30px;
  border-radius: 5px;
  display: flex;
  justify-content: space-around;
  
}
</style>
