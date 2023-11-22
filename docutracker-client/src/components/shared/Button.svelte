<script lang="ts">
  import { fade } from "svelte/transition";

  export let hoverized = false;
  export let disabled = false;
</script>

<button
  class:hovered={hoverized}
  class:t={disabled}
  {disabled}
  transition:fade={{ duration: 200, delay: 200 }}
  on:click|stopPropagation
>
  <slot />
</button>

<style>
  button {
    width: 100%;
    height: 2rem;
    border: none;
    color: var(--background);
    background: var(--border-hover-color);
    border-radius: 5px;
    cursor: pointer;
    transition: ease-in-out 500ms;
  }

  button.hovered:hover {
    box-shadow: 5px 5px 25px var(--main-col-1);
  }

  button.t {
    background-color: var(--main-col-1);
    pointer-events: none;
  }

  button.t:hover {
    box-shadow: none;
  }
</style>
