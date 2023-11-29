<script lang="ts">
  import { fly } from "svelte/transition";
  export let shortcutData = "Hello from Shortcut Wrapper";
</script>

<div
  in:fly={{ x: 1000, duration: 800, delay: 100 }}
  out:fly={{ x: 1000, duration: 800, delay: 100 }}
>
  {shortcutData}
</div>

<style>
  div {
    position: absolute;
    top: 3rem;
    right: 0;
    background-color: var(--main-col-5);
    height: 95vh;
    width: 100%;
  }
</style>
