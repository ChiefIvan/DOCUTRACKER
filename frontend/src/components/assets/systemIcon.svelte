<script>
  export let active = false;
</script>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  ><path
    class:icon-active={active}
    d="M13 18v2h4v2H7v-2h4v-2H2.992A.998.998 0 0 1 2 16.992V4.008C2 3.451 2.455 3 2.992 3h18.016c.548 0 .992.449.992 1.007v12.985c0 .557-.455 1.008-.992 1.008H13Z"
  /></svg
>

<style>
  svg {
    width: calc(var(--size-1) * 0.75);
    height: calc(var(--size-1) * 0.75);
    cursor: pointer;

    & path {
      fill: var(--main-col-1);
    }

    & path.icon-active {
      fill: var(--ico-actv);
    }
  }
</style>
