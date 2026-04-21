<script lang="ts">
	import { setContext } from 'svelte';
	import { Topbar } from '@/components/layouts/topbar';

	type Stage = 'form' | 'loading' | 'report';

	let { children } = $props();

	let stage = $state<Stage>('form');
	let sessionId = $state('');
	let reportMarkdown = $state('');

	function reset() {
		stage = 'form';
		sessionId = '';
		reportMarkdown = '';
	}

	setContext('app', {
		get stage() {
			return stage;
		},
		set stage(v: Stage) {
			stage = v;
		},
		get sessionId() {
			return sessionId;
		},
		set sessionId(v: string) {
			sessionId = v;
		},
		get reportMarkdown() {
			return reportMarkdown;
		},
		set reportMarkdown(v: string) {
			reportMarkdown = v;
		},
		reset
	});
</script>

<div class="flex min-h-screen flex-col">
	<Topbar />
	<main class="flex flex-1 flex-col bg-s-background">
		{@render children()}
	</main>
</div>
