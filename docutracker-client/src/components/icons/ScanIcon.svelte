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
        fill="currentColor"
        d="M13 9h5l-5-5v5ZM6 22q-.825 0-1.413-.588T4 20v-3h16v3q0 .825-.588 1.413T18 22H6Zm-5-7v-2h22v2H1Zm3-4V4q0-.825.588-1.413T6 2h8l6 6v3H4Z"
      /></svg
    >
  </div>
{:else}
  <div
    use:tooltip={{
      arrow: false,
      content: "Scan Document",
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
        fill="currentColor"
        d="M13 9h5l-5-5v5ZM6 22q-.825 0-1.413-.588T4 20v-3h16v3q0 .825-.588 1.413T18 22H6Zm-5-7v-2h22v2H1Zm3-4V4q0-.825.588-1.413T6 2h8l6 6v3H4Z"
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
      transition: all ease-in-out 300ms;

      & path {
        transition: all ease-in-out 300ms;
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
