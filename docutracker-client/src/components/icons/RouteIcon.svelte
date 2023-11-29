<script>
  import { dark, navExpand } from "../../store";
  import { tooltip } from "../shared/Tooltip";

  export let active = false;
</script>

{#if $navExpand}
  <div>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
      ><path
        class:dark={$dark}
        class:active
        d="M11 10H5L3 8l2-2h6V3l1-1l1 1v1h6l2 2l-2 2h-6v2h6l2 2l-2 2h-6v6a2 2 0 0 1 2 2H9a2 2 0 0 1 2-2z"
      /></svg
    >
  </div>
{:else}
  <div
    use:tooltip={{
      arrow: false,
      content: "Register Route",
      animation: "perspective-subtle",
      theme: "tooltip",
      offset: [0, 20],
      placement: "right",
    }}
  >
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
      ><path
        class:dark={$dark}
        class:active
        d="M11 10H5L3 8l2-2h6V3l1-1l1 1v1h6l2 2l-2 2h-6v2h6l2 2l-2 2h-6v6a2 2 0 0 1 2 2H9a2 2 0 0 1 2-2z"
      /></svg
    >
  </div>
{/if}

<style>
  div {
    display: flex;
    align-items: center;

    & svg {
      min-width: 1.8rem;
      max-width: 1.8rem;
      cursor: pointer;
      transition: all ease-in-out 500ms;

      & path {
        transition: all ease-in-out 500ms;
        fill: var(--main-col-1);
      }

      & path.active {
        fill: var(--icon-active-color);
      }

      & path.dark {
        fill: var(--icon-dark);
      }
    }
  }
</style>
