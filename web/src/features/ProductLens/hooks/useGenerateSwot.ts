import { createMutation } from '@tanstack/svelte-query';
import { generateSwot } from '../api/swot-generate';

export const useGenerateSwot = () => {
	return createMutation(() => ({
		mutationFn: generateSwot
	}));
};
