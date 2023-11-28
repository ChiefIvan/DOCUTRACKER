<script>
  export let name = "Hello from Shortcut Wrapper";
</script>

<div>
  {name}
</div>

<style>
  div {
    position: absolute;
    inset: 0;
    z-index: 5;
    color: var(--component-active);
  }
</style>
