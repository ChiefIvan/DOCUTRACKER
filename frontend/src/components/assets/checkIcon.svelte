<script>
  import { dark } from "../../stores";
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<svg
  class:dark={$dark}
  on:click
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
  ><path
    class:dark={$dark}
    fill="currentColor"
    d="m9 20.42l-6.21-6.21l2.83-2.83L9 14.77l9.88-9.89l2.83 2.83L9 20.42Z"
  /></svg
>

<style>
  svg {
    width: calc(var(--size-1) * 0.9);
    height: calc(var(--size-1) * 0.9);
    transition: all ease-in-out var(--dur2);
    cursor: pointer;
    border-radius: 50%;
    padding: calc(var(--size-6) * 0.3);

    & path {
      fill: var(--main-col-1);
      transition: all ease-in-out var(--dur);
    }
  }

  svg:hover {
    background-color: var(--main-col-1);
  }

  svg.dark:hover {
    background-color: var(--dark-main-col-2);
  }

  svg:hover path {
    fill: var(--bg);
  }
</style>
