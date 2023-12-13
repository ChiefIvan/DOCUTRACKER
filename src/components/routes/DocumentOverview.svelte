<script lang="ts">
  import { type Document } from "../../store";
  import { scale } from "svelte/transition";

  import CheckAuthenticity from "../shared/CheckAuthenticity.svelte";
  export let authToken = "";

  export let documents: Document;

  // const handleExpand = (name: string) => {
  //   // This function is used to expand the whatever use has selected
  // };

  let name = "";
</script>

<svelte:head>
  <title>DOCUTRACKER | Document Overview</title>
</svelte:head>

<CheckAuthenticity {authToken} on:user></CheckAuthenticity>

<main>
  {#if documents}
    {#each documents as document}
      {#if document.codeData}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div
          class="credential-wrapper"
          on:click={() => (name = document.documentName)}
        >
          {document.documentName}
        </div>
      {/if}
    {/each}
  {/if}
  {#if name.length}
    <div transition:scale class="document-wrapper">
      <button on:click={() => (name = "")}>Go back</button>
      {#each documents as document}
        {#if document.documentName === name}
          {document.documentName}
          {document.documentDescription}
          {document.documentRegDate}
          {document.codeData}
        {/if}
      {/each}
    </div>
  {/if}
</main>

<style>
  main {
    height: calc(100vh - 43.16px);
    text-align: center;
    position: relative;

    & div.credential-wrapper {
      transition: all ease-in-out 300ms;
      cursor: pointer;
      margin-top: 1rem;
      text-align: left;
      padding: 0.5rem 1rem;
      font-weight: 700;
      color: var(--scroll-color);
      font-size: 1;
      display: inline-block;
      width: 98%;
      border: 1px solid var(--header-color);
      border-radius: 0.5rem;
    }

    & div.credential-wrapper:hover {
      background-color: var(--header-color);
    }

    & div.document-wrapper {
      position: absolute;
      inset: 0;
      background-color: var(--scroll-color);
    }
  }
</style>
