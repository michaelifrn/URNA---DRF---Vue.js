<template>
    <div class="screenVotes">
        <div v-for="vote of report" :key="vote.id" class="screenVote">

            <div class="candidateName">
                {{ vote.name }}
            </div>
            <p>Total de votos:</p>
            <div class="numberVotes">
                {{ vote.votes }}
            </div>

        </div>

    </div>
</template>

<script>

export default{
    name: 'screenVotes',
    props: {
        report: Array
    }
}   
    

</script>

<style>
    .screenVotes {
        display: flex;
        align-items: center;
        justify-content: space-around;
        width: 100%;
        height: 100%;
        gap: 30px;
    }
    .screenVote {
        width: 250px;
        height: 250px;
        background-color: var(--ballot-box-screen-color);
        border-radius: 5px;
        border: 2px solid var(--light-border-color);
        padding: 20px;
        color: var(--dark-text-color);
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }



    .candidateName {
        font-size: 18px;
        font-weight: bold;
    }

    .numberVotes {
        width: 100px;
        height: 100px;
        background-color:var(--ballot-box-background-color);
        font-size: 30px;
        font-weight: bold;
        color: var(--dark-text-color);
        display: flex;
        justify-content: center;
        align-items: center;
        border: 5px;
        border: 2px solid var(--light-border-color);
    }

  

</style>