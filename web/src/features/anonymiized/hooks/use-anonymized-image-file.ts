import { createMutation } from '@tanstack/svelte-query';
import { callAnonymizedImageFile } from '../api/anonymized-image-file';

export const useAnonymizedImageFile = () => {
	return createMutation(() => ({
		mutationFn: callAnonymizedImageFile
	}));
};
