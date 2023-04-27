<template>
    <div class="screen">

        <div v-if="screenOutput != 'voted'" class="vote">

            <div class="screenInput">
            
              <form id="vote" @submit.prevent="voted">
                
                <label>Matrícula:</label>
                <input type="number" v-model="voteRegister.registration">
                <label>Número:</label>
                <input type="number" v-model="voteRegister.number">
    
              </form>

            </div>

            <div class="actions">

                <button class="orange" @click="clearNumber">CORRIGE</button>
                <button type="submit" form= "vote" class="green">CONFIRMA</button>

            </div>
        
        </div>

        <div v-if="screenOutput == 'voted'" class="registration">
        
                
            <h1>Aperte o botão para iniciar.</h1>

            <div class="actions">

                <button class="white" @click="start">INICIAR</button>

            </div>


        </div>
        
    </div>
</template>

<script>

import functions from '@/services/candidates';

export default{
    methods:{
    voted(){
      functions.vote(this.voteRegister).then( ()=> {
        alert("Voto registrado!")
        this.screenOutput = 'voted'
        this.voteRegister.registration = null
        this.voteRegister.number = null
      }).catch(error => {
        if (error.response){
            alert(error.response.data.error)
        }else{
            console.log('error: ', error)
        }

      })
    },
    clearNumber() {
    this.voteRegister.registration = null;
      this.voteRegister.number = null;
    },
    start() {
    this.screenOutput = '';
    }
  },
    name: 'screenOutput',

    data(){
        return {
        screenOutput: 'voted',
        voteRegister: {
            registration: null,
            number: null
            }
        }
    }
}

</script>

<style>

    .screen {
        width: 100%;
        height: 100%;
        background-color: #808080;
        border-radius: 7px;
        border: 2px solid var(--light-border-color);
        padding: 20px;
        color: var(--dark-text-color);
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .screenInput form {
        display: flex;
        flex-direction: column;
        font-size: 20px;
    }

    .screenInput form input {
        width: 450px;
        height: 40px;
        margin-bottom: 20px;
        font-size: 20px;
    }

    .screenInput form input[type=number]::-webkit-inner-spin-button,
    .screenInput form input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }


    .actions {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-around;
        border-radius: 7px;
    }

    .actions button {
        color: var(--dark-text-color);
        font-size: 15px;
        border-radius: 5px;
        width: 30%;
        height: 50px;
    }

    .white {
        background-color: var(--ballot-box-white-button-color);
    }

    .orange {
        background-color: var(--ballot-box-correct-button-color);
    }

    .green {
        background-color: var(--ballot-box-confirm-button-color);
    }

</style>