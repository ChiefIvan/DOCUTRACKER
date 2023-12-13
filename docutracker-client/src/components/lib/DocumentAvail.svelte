<script lang="ts">
  import {
    activeDocument,
    docNameExpand,
    documentTimeZone,
    dark,
    type Document,
  } from "../../store";
  import TriangleIcon from "../icons/TriangleIcon.svelte";

  export let document: Document;
  export let inner = false;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
  class="name-wrapper"
  class:inner
  on:click={() => ($docNameExpand = !$docNameExpand)}
>
  <div class="document-name-wrapper">
    {#if $activeDocument}
      {#if document && document.length}
        {#each document as route (route)}
          {#if route.documentName === $activeDocument}
            <span>{route.documentName}</span>
          {/if}
        {/each}
      {/if}
    {:else}
      <span>Select a Document</span>
    {/if}
    <TriangleIcon rotate={$docNameExpand}></TriangleIcon>
  </div>
</div>

<div
  class="choice-wrapper"
  class:wrapper-expand={$docNameExpand}
  class:dark={$dark}
  class:inner
>
  <ul class="name-wrapper">
    {#if document && document.length}
      {#each document as route (route)}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
        {#if route.codeData && route.codeData.length}
          <li
            on:click={() => {
              $activeDocument = route.documentName;
              $documentTimeZone = route.documentRegDate;
              $docNameExpand = false;
            }}
          >
            <span
              class="document-name"
              class:active={$activeDocument === document.documentName}
              >{route.documentName}</span
            >
          </li>
        {/if}
      {/each}
    {/if}
  </ul>
</div>

<style>
  div.name-wrapper {
    transition: all ease-in-out 300ms;
    border-radius: 0.5rem;
    padding: 0 0.5rem;

    & div.document-name-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
      column-gap: 0.5rem;
      cursor: pointer;
      height: 2rem;

      & span {
        transition: all ease-in-out 300ms;
        color: var(--scroll-color);
      }
    }
  }

  div.inner {
    border-radius: 0;
    padding: 0;
    background-color: var(--main-col-7);
  }

  div.name-wrapper:hover {
    background-color: var(--main-col-2);
  }

  /* div.name-wrapper:hover div.document-name-wrapper span {
    color: var(--background);
  } */

  div.choice-wrapper {
    display: grid;
    grid-template-rows: 0fr;

    overflow: hidden;
    position: fixed;
    top: 3.5rem;
    left: 16rem;
    z-index: 1;

    transition: all ease-in-out 400ms;
    background-color: var(--background);
    box-shadow: 5px 5px 25px lightgray;
    border-radius: 0.5rem;
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.3);

    & ul.name-wrapper {
      min-height: 0;

      & li {
        display: flex;
        align-items: center;
        column-gap: 0.5rem;
        margin: 0.2rem;
        padding: 0.2rem 0.5rem;
        border-radius: 0.4rem;
        transition: all ease-in-out 500ms;
        cursor: pointer;

        & span.document-name {
          color: var(--main-col-1);
        }

        & span.active {
          color: var(--icon-active-color);
        }
      }

      & li:hover {
        background-color: var(--main-col-2);
      }
    }
  }

  div.inner {
    top: 5.5rem;
    left: 8rem;
  }

  div.wrapper-expand {
    grid-template-rows: 1fr;
  }

  div.dark {
    background-color: var(--dark-main-col-1);
    box-shadow: none;
  }
</style>
