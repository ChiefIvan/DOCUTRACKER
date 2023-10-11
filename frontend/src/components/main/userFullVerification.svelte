<script>
  import { fly } from "svelte/transition";
  import { quintInOut } from "svelte/easing";
</script>

<section
  transition:fly={{
    x: 700,
    delay: 0,
    duration: 1000,
    easing: quintInOut,
    // axis: "x",
  }}
>
  Hello
</section>

<style>
  section {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    z-index: 3;

    width: calc(var(--size-4) * 3);
    background-color: brown;
  }
</style>
