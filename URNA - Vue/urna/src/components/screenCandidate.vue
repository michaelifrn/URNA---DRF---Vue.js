<template>
    <div class="screenCandidates">

        <div v-for="candidate of candidatesList" :key="candidate.id" class="screenCandidate">
            
            <div class="candidateName">
                {{ candidate.name }}
            </div>

            <div class="candidateNumber">
                {{ candidate.number }}
            </div>

        </div>

    </div>
</template>

<script>

export default{
    name: 'screenCandidates',
    props: {
        candidatesList: Array
    }
}   
    

</script>

<style>
    .screenCandidates {
        display: flex;
        align-items: center;
        justify-content: space-around;
        width: 100%;
        height: 100%;
        gap: 30px;
        margin-bottom: 40px;
        margin-top: 40px;
    }
    .screenCandidate {
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

    .candidateNumber {
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