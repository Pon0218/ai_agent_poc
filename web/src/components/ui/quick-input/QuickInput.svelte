<script lang="ts">
	import { untrack } from 'svelte';
	import { cn } from '@/utils/cn';

	let {
		placeholder = '貼上你的產品網址 — https://example.com',
		initialValue = '',
		class: className,
		onsubmit
	}: {
		placeholder?: string;
		initialValue?: string;
		class?: string;
		onsubmit: (value: string) => void;
	} = $props();

	// untrack: intentionally capture only the initial value (uncontrolled input pattern)
	let value = $state(untrack(() => initialValue));

	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();
		onsubmit(value);
	}
</script>

<form
	onsubmit={handleSubmit}
	class={cn(
		'flex max-w-160 items-center gap-2 rounded-full border border-pl-rule bg-white px-5.5 py-2',
		'shadow-[0_1px_0_rgba(0,0,0,0.02),0_12px_30px_-18px_rgba(0,0,0,0.18)]',
		'transition-[border-color,box-shadow]',
		'focus-within:border-pl-ink focus-within:shadow-[0_1px_0_rgba(0,0,0,0.02),0_14px_36px_-16px_rgba(0,0,0,0.25)]',
		className
	)}
>
	<input
		bind:value
		type="text"
		{placeholder}
		autocomplete="off"
		class="flex-1 border-0 bg-transparent py-3 text-[16px] text-pl-ink outline-none placeholder:text-pl-ink-3"
	/>
	<button
		type="submit"
		class="inline-flex cursor-pointer items-center gap-2 rounded-full bg-pl-accent px-5 py-3 text-[14px] font-medium whitespace-nowrap text-pl-bg transition-colors hover:bg-pl-accent-h"
	>
		Analyze <span>→</span>
	</button>
</form>
