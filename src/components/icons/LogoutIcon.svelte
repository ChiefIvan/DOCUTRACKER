<script>
  import { fade } from "svelte/transition";
  import { dark } from "../../store";
  import { tooltip } from "../shared/Tooltip";
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
  on:click|stopPropagation
  class="logout-icon"
  use:tooltip={{
    arrow: false,
    content: "Logout",
    animation: "perspective-subtle",
    theme: "tooltip",
    offset: [0, 20],
    placement: "right",
  }}
>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    on:click
    transition:fade={{ duration: 200, delay: 200 }}
    ><path class:dark={$dark} d="m2 12l5 4v-3h9v-2H7V8z" /><path
      class:dark={$dark}
      d="M13.001 2.999a8.938 8.938 0 0 0-6.364 2.637L8.051 7.05c1.322-1.322 3.08-2.051 4.95-2.051s3.628.729 4.95 2.051s2.051 3.08 2.051 4.95s-.729 3.628-2.051 4.95s-3.08 2.051-4.95 2.051s-3.628-.729-4.95-2.051l-1.414 1.414c1.699 1.7 3.959 2.637 6.364 2.637s4.665-.937 6.364-2.637c1.7-1.699 2.637-3.959 2.637-6.364s-.937-4.665-2.637-6.364a8.938 8.938 0 0 0-6.364-2.637z"
    /></svg
  >
</div>

<style>
  div.logout-icon {
    position: absolute;
    inset: 0;
    text-align: center;

    & svg {
      width: 1.8rem;
      height: 1.8rem;
      cursor: pointer;
      transition: all ease-in-out 500ms;
      border-radius: 50%;
      padding: 0.2rem;

      & path {
        fill: var(--main-col-1);
        transition: all ease-in-out 500ms;
      }

      & path.dark {
        fill: var(--background);
      }
    }

    & svg:hover {
      background-color: var(--main-col-1);
    }

    & svg:hover path {
      fill: var(--background);
    }
  }
</style>
